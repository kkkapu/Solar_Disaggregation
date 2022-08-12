import pandas as pd


class Helper:
    def __init__(self, withoutsolar):
        self.total_pairs = []
        self.visited = set()
        self.max_loadgap = max(withoutsolar["consumption"]) - min(
            withoutsolar["consumption"]
        )

    def get_similarity_score(self, data_copy, withoutsolar, i, j):
        kk1 = withoutsolar[i : i + 1].index[0]
        kk2 = withoutsolar[j : j + 1].index[0]

        grid1 = data_copy[data_copy.index == kk1]["grid"].values[0]
        grid2 = data_copy[data_copy.index == kk2]["grid"].values[0]

        score = 0
        n = 1.5
        score += (
            365 ** (1 / n)
            - abs(withoutsolar.iloc[i]["dayofyear"] - withoutsolar.iloc[j]["dayofyear"])
            ** (1 / n)
        ) / 365 ** (1 / n)
        n = 2
        score += (
            1440 ** (1 / n)
            - abs(
                withoutsolar.iloc[i]["minuteofday"]
                - withoutsolar.iloc[j]["minuteofday"]
            )
            ** (1 / n)
        ) / 1440 ** (1 / n)
        n = 3
        score += (
            self.max_loadgap ** (1 / n)
            - abs(
                withoutsolar.iloc[i]["consumption"]
                - withoutsolar.iloc[j]["consumption"]
            )
            ** (1 / n)
        ) / self.max_loadgap ** (1 / n)
        self.total_pairs.append([i, j, score])

    def pair_selection(self, data_copy, withoutsolar, target_pair_number):

        k = 10
        for step in range(1, k + 1):
            for i in range(len(withoutsolar)):
                if i + step <= len(withoutsolar) - 1:
                    self.get_similarity_score(data_copy, withoutsolar, i, i + step)

        self.total_pairs = sorted(self.total_pairs, key=lambda x: -x[2])
        for i, j, k in self.total_pairs:
            if (i, j) not in self.visited:
                self.visited.add((i, j))
            if len(self.visited) >= target_pair_number:
                break
        return self.visited

    def training_data_constuct(self, data_copy, withoutsolar):
        train_pairs_without = []
        train_pairs = []

        for p1, p2 in self.visited:
            train_pairs_without.append([p1, p2])
            train_pairs.append(
                [withoutsolar[p1 : p1 + 1].index, withoutsolar[p2 : p2 + 1].index]
            )

        df = pd.DataFrame(columns=data_copy.columns)
        for i in train_pairs:
            df = pd.concat([df, data_copy[data_copy.index == i[0][0]]], axis=0)
            df = pd.concat([df, data_copy[data_copy.index == i[1][0]]], axis=0)

        return df
