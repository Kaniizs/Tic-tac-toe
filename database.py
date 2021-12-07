import csv


class Db:
    def __init__(self) -> None:
        self.database = []
        with open('kongkang.csv', 'r') as data:
            now_data = csv.DictReader(data)
            for each_data in now_data:
                self.database.append(each_data)

    def update_data(self, mode, player1, player2, winner):
        new_data = {'mode': mode, 'player1': player1,
                    'player2': player2, 'winner': winner}
        self.database.append(new_data)
        self.update_file()

    def update_file(self):

        with open('kongkang.csv', 'w') as data:
            writer = csv.DictWriter(
                data, fieldnames=['mode', 'player1', 'player2', 'winner'])

            writer.writeheader()
            for each_data in self.database:
                writer.writerow(each_data)
