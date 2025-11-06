import csv

def save_to_csv(filename, data):
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f" บันทึก {filename} เรียบร้อยแล้ว")

def read_csv(filename):
    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)
