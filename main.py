import json
import requests
import time

input_filename = "input.txt"
output_filename = "output.txt"
api = "http://rosreestr.subnets.ru/?get=num&format=json&num="
delay = 0.2


input_file = open(input_filename, "r", encoding="utf-8")

try:
    output_file = open(output_filename, "w", encoding="utf-8")
except IOError:
    input_file.close()
input_line = input_file.readline()

while input_line != "":
    try:
        input_arr = input_line.split(",")
        phone_num = input_arr[0].strip()
        phone_carrier = input_arr[1].strip()
        res = requests.get(api + phone_num)
        answer = json.loads(res.content)
        if "0" in answer:
            answer_carrier = answer["0"]["operator"]
            is_match = answer_carrier == phone_carrier
            output_file.write(phone_num + "," + phone_carrier +
                                  "," + answer_carrier + "," + str(int(is_match)) + "\n")
        else:
            output_file.write(phone_num + "," + phone_carrier + "," +
                                  json.dumps(answer, ensure_ascii=False) + ",2" + "\n")
    except BaseException as exception:
        output_file.write(phone_num + "," + phone_carrier + "," + exception)
    time.sleep(delay)
    input_line = input_file.readline()

# breakpoint()
input_file.close()
output_file.close()
