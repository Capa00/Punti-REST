import math
import multiprocessing
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


def get_noise(list_, coeff_, noise_, x_, y_):
    list_.append(coeff_ * noise_([x_, y_]))


def main():
    import matplotlib.pyplot as plt
    from perlin_noise import PerlinNoise

    def falloff_map(island_size, x_, y_):
        return x/island_size
        x_ *= island_size
        y_ *= island_size
        len_ = island_size*0.5

        # x/2??
        min_ = min(x_, len_-x_)
        min_ = min(min_, y_)
        min_ = min(min_, len_-y_)

        return min_/len_

    seed = 20  # random.randint(1, 1000)
    noise1 = PerlinNoise(octaves=3, seed=seed)
    noise2 = PerlinNoise(octaves=6, seed=seed)
    noise3 = PerlinNoise(octaves=12, seed=seed)

    xpix, ypix = 100, 100
    x0, y0 = 20, 20
    pic_coeff = []
    pic_noise = []

    start = datetime.now()

    for i in range(ypix):
        coeffs = []
        noise = []
        for j in range(xpix):
            x = x0+(i / xpix)
            y = y0+(j / ypix)

            noise_val = []

            with ThreadPoolExecutor(max_workers=3) as executor:
                executor.submit(get_noise, noise_val, 1, noise, x, y)
                executor.submit(get_noise, noise_val, 0.5, noise2, x, y)
                executor.submit(get_noise, noise_val, 0.25, noise3, x, y)

            noise_val = sum(noise_val)

            # noise_val = noise1([x, y])
            # noise_val += 0.5 * noise2([x, y])
            # noise_val += 0.25 * noise3([x, y])

            x -= x0
            y -= y0

            texture = '  ._-*o§##'
            k = falloff_map(xpix, i, j)
            # alto sx min(j/xpix, i/ypix)
            # basso sx min(j/xpix, (ypix-i)/ypix))
            # sx min(j/xpix, min((ypix-i, i))/ypix))
            lenx = xpix/2
            leny = ypix/2
            dx = min(j/lenx, (lenx-j)/lenx)

            lambda_ = -3.9
            k = math.exp( -lambda_ * x )
            c = math.exp( -lambda_ * y )

            index = int(len(texture) * min(k, c)) - 1
            # index = int(k)*len(texture)
            # row.append(texture[index])
            coeff = min(k, c)

            coeffs.append(coeff)
            noise.append(noise_val)

        pic_coeff.append(coeffs)
        pic_noise.append(noise)

    # for r in pic_noise:
    #     print(r)

    pic = [[0 for i in range(len(pic_coeff))] for j in range(len(pic_coeff))]

    min_pick = abs(min(min(pic_noise)))
    pic_noise = [[min_pick + p for p in pi] for pi in pic_noise]  # porto il noise a 0 minimo assoluto

    min_pick = abs(min(min(pic_noise)))
    max_pick = abs(max(max(pic_noise)))
    print(f"{max_pick=}")
    print(f"{min_pick=}")

    for i in range(len(pic_coeff)):
        for j in range(len(pic_coeff)):
            pic[i][j] = pic_coeff[i][j] * pic_noise[i][j]

    print( datetime.now() - start)

    fig = plt.figure(figsize=(8, 8))
    imgs = [pic_coeff, pic_noise, pic]
    for i in range(1, 3 + 1):
        img = imgs[i-1]
        fig.add_subplot(1, 3, i)
        plt.imshow(img, cmap='terrain')
    plt.show()


class Island:

    def __init__(self):
        super(Island, self).__init__()

    def build(self):
        from perlin_noise import PerlinNoise

        n = 50
        w = n
        h = n

        seed = 50
        noise_matr = [[0 for i in range(h)] for j in range(w)]

        noises = [
            (PerlinNoise(octaves=3, seed=seed), 1),
            (PerlinNoise(octaves=6, seed=seed), 0.5),
            (PerlinNoise(octaves=12, seed=seed), 0.25),
        ]

        start = datetime.now()
        # Gestire race condition
        [threading.Thread(target=self._make_noise(noise_matr, noise[0], noise[1], mutex)).start() for noise in noises]
        [wait.acquire() for i in noises]

        print(datetime.now() - start)

        min_pick = abs(min(min(noise_matr)))
        noise_matr = [[min_pick + p for p in pi] for pi in noise_matr]  # porto il noise a 0 minimo assoluto
        print(min(min(noise_matr)))

        fog_noise = self._make_fog_noise(noise_matr)
        island = [[0 for i in range(h)] for j in range(w)]
        print(min(min(fog_noise)))


        for i in range(len(island)):
            for j in range(len(island[0])):
                island[i][j] = noise_matr[i][j] * fog_noise[i][j]

        pyplottalo(fog_noise, noise_matr, island)

    def _make_fog_noise(self, matrice):
        lenx = len(matrice[0])
        leny = len(matrice)
        lambda_ = -5

        fog = []

        for i in range(leny):
            y = i / leny
            fog_row = []

            for j in range(lenx):
                x = j / lenx
                fog_row.append(
                    min([
                        math.exp(-lambda_ * x),
                        math.exp(-lambda_ * y),
                        math.exp(-lambda_ * (1 - x)),
                        math.exp(-lambda_ * (1 - y)),
                    ])
                )

            fog.append(fog_row)
        return fog

    def _make_noise(self, matrice, noise, coeff, lock):
        lenx = len(matrice[0])
        leny = len(matrice)
        step = 0.03

        def wrap():
            y = -step
            x = -step
            for i in range(leny):
                y += step
                for j in range(lenx):
                    x += step

                    val = coeff * noise([x, y])

                    lock.acquire()
                    matrice[i][j] += val
                    lock.release()
                x = -step

            wait.release()

        return wrap


mutex = multiprocessing.Lock()
wait = multiprocessing.Semaphore()

def pyplottalo(*matrici):
    from matplotlib import pyplot as plt
    fig = plt.figure(figsize=(8, 8))
    for i in range(1, len(matrici) + 1):
        img = matrici[i - 1]
        fig.add_subplot(1, 3, i)
        plt.imshow(img, cmap='terrain')
    plt.show()


if __name__ == '__main__':
    Island().build()
