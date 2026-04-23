# handel storage Saving + loading JSON
import json

class TalentRepository:
    

    def save(self, talent):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
        except:
            data = []

        data.append(talent.to_dict())

        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)
