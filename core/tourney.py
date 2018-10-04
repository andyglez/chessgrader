from core import game


class AllVsAll:
    def __init__(self, mods):
        self.mods = mods
        self.points = None

    def reset(self):
        self.points = [0.] * len(self.mods)

    def __iter__(self):
        self.reset()

        for ix, modx in enumerate(self.mods):
            for iy, mody in enumerate(self.mods):
                if ix == iy:
                    continue

                def callback(winner):
                    if winner == +1:
                        self.points[ix] += 1
                    elif winner == -1:
                        self.points[iy] += 1
                    else:
                        self.points[ix] += .5
                        self.points[iy] += .5

                yield modx, mody, callback

    def run(self, args):
        for p0, p1, callback in self:
            if args.verbose >= 1:
                print("-- {0}(W) VS {1}(B) --".format(p0.NAME, p1.NAME))

            winner, error = game.play(p0.Player, p1.Player, args)
            callback(winner)

        self.results()

    def results(self):
        print("{0:5}| {1:25}| {2}".format("Score", "Name", "Author"))
        for mod, score in zip(self.mods, self.points):
            print("{0:5}| {1:25}| {2}".format(score, mod.NAME, ', '.join(mod.AUTHOR)))
