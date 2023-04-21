import json


class Data:
    def __init__(self, path):
        self.path = path
        self.file_cont = ""
        self.obj = []

    def parse_json(self):
        with open(self.path, 'r') as f:
            self.obj = json.loads(self.file_cont)
        
    def load_file(self):
        with open(self.path) as f:
            self.file_cont = f.read()

    def get_all_titles(self):
        out = []
        for i in self.obj:
            out.append([f"{x[0]}: {x[1]}" for x in i.items()])
        return out
    
    def get_best_films(self):
        out = []
        for i in self.obj:
            if int(i["rating"]) > 8:
                out.append([f"{x[0]}: {x[1]}" for x in i.items()])
        return out

    def get_worst_films(self):
        out = []
        for i in self.obj:
            if int(i["rating"]) < 5:
                out.append([f"{x[0]}: {x[1]}" for x in i.items()])
        return out

    def get_by_year(self, year):
        out = []
        for i in self.obj:
            if i["year"] == year:
                out.append([f"{x[0]}: {x[1]}" for x in i.items()])
        return out
    
    def get_by_country(self, country):
        out = []
        for i in self.obj:
            if i["country"] == country:
                out.append([f"{x[0]}: {x[1]}" for x in i.items()])
        return out
    
    def save_to_txt(self, path):
        with open(path, "w") as f:
            for line in self.obj:
                f.write(str(line) + "\n")

    

