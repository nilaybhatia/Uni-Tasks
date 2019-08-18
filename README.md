# Unicode-Tasks
## Tasks for Unicode interviews

### Task 1:
We were given a comma separated string of integers in binary format and had to check which of them are divisible by 5. I've accomplished this task using standard inbuilt functions like `filter`, `join`, etc.

INPUT: 
```
input_string = "010, 1111, 1010, 10010, 100000, 10100, 110"
```
OUTPUT:

![Task 1 output](/images/task_1_output.png)

---

### Task 2:
Had to display SpaceX launch data in JSON format using data fetched from the API. Did not involve any templating. Had to just return an HttpResponse object.

OUTPUT:

![Task 2 output](/images/task_2_output.png)

---
### Task 3:
We had to use an HTML page as a template in this task. I've dispalyed the data in the form of a table. Also did a bit of inline formatting in the template for a more pleasing look.

OUTPUT:

![Task 3 output](/images/task_3_output.png)

---
### Task 4:
Had to first store the fetched data in models and then access the data usig QuerySet object.

OUTPUT:
Same as previous.

### Additional feature added:
It is highly likely that the user will be interested in questions related to the SpaceX company. Hence I've used the StackExchange API to fetch recent questions with [```spacex```](https://space.stackexchange.com/questions/tagged/spacex) tag.
![Recent question on SpaceX](/images/spacex_questions.png)

---

## Instructions to run the project locally
1. git clone https://www.github.com/nilaybhatia/Forum.git
2. cd Forum/
3. Activate your virtual environment (help [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/))
4. pip install -r requirements.txt (Assuming pip is installed)
5. python manage.py runserver




