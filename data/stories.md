## happy greet
* greet
    - utter_greet
    - utter_sayname
    - action_set_answers_null
## start path
* procurement
    - utter_question_1
> Check_question1

<!--     - slot{"name":"Rahul"}
* saidname{"name":"Rahul"}
    - slot{"name":"Rahul"}
    - utter_sayname -->

## story 99
> Check_question1

* said_no
    - slot{"answer1":"no"}
    - action_answer1_submit
    - action_hello_world
<!--     - action_save_details -->


## story path R1
> Check_question1

* said_yes
    - slot{"answer1":"yes"}
    - action_answer1_submit
    - utter_question_2
> Check_question2

## story 0

> Check_question2

* said_yes
    - slot{"answer2":"yes"}
    - action_answer2_submit
    - utter_0
<!--     - action_save_details -->

## story path R2

> Check_question2

* said_no
    - slot{"answer2":"no"}
    - action_answer2_submit
    - utter_question_3
    
> Check_question3

## story 1
> Check_question3

* said_no
    - slot{"answer3":"no"}
    - action_answer3_submit
    - utter_1
<!--     - action_save_details -->

## story 2
> Check_question3

* said_yes
    - slot{"answer3":"yes"}
    - action_answer3_submit
    - utter_question_4
    
* said_no
    - slot{"answer4":"no"}
    - action_answer4_submit
    - utter_question_5
    
* said_no
    - slot{"answer5":"no"}
    - action_answer5_submit
    - utter_question_6
    
* said_no
    - slot{"answer6":"no"}
    - action_answer6_submit
    - utter_2

## story 3
> Check_question3

* said_yes
    - slot{"answer3":"yes"}
    - action_answer3_submit
    - utter_question_4
    
* said_no
    - slot{"answer4":"no"}
    - action_answer4_submit
    - utter_question_5
    
* said_no
    - slot{"answer5":"no"}
    - action_answer5_submit
    - utter_question_6
    
* said_yes
    - slot{"answer6":"yes"}
    - action_answer6_submit
    - utter_3

## story 4
> Check_question3

* said_yes
    - slot{"answer3":"yes"}
    - action_answer3_submit
    - utter_question_4
    
* said_no
    - slot{"answer4":"no"}
    - action_answer4_submit
    - utter_question_5
    
* said_yes
    - slot{"answer5":"yes"}
    - action_answer5_submit
    - utter_question_6
    
* said_no
    - slot{"answer6":"no"}
    - action_answer6_submit
    - utter_4

## story 5
> Check_question3

* said_yes
    - slot{"answer3":"yes"}
    - action_answer3_submit
    - utter_question_4
    
* said_no
    - slot{"answer4":"no"}
    - action_answer4_submit
    - utter_question_5
    
* said_yes
    - slot{"answer5":"yes"}
    - action_answer5_submit
    - utter_question_6
    
* said_yes
    - slot{"answer6":"yes"}
    - action_answer6_submit
    - utter_5

## story 6
> Check_question3

* said_yes
    - slot{"answer3":"yes"}
    - action_answer3_submit
    - utter_question_4
    
* said_yes
    - slot{"answer4":"yes"}
    - action_answer4_submit
    - utter_question_5
    
* said_no
    - slot{"answer5":"no"}
    - action_answer5_submit
    - utter_question_6
    
* said_no
    - slot{"answer6":"no"}
    - action_answer6_submit
    - utter_6

## story 7
> Check_question3

* said_yes
    - slot{"answer3":"yes"}
    - action_answer3_submit
    - utter_question_4
    
* said_yes
    - slot{"answer4":"yes"}
    - action_answer4_submit
    - utter_question_5
    
* said_no
    - slot{"answer5":"no"}
    - action_answer5_submit
    - utter_question_6
    
* said_yes
    - slot{"answer6":"yes"}
    - action_answer6_submit
    - utter_7

## story 8
> Check_question3

* said_yes
    - slot{"answer3":"yes"}
    - action_answer3_submit
    - utter_question_4
    
* said_yes
    - slot{"answer4":"yes"}
    - action_answer4_submit
    - utter_question_5
    
* said_yes
    - slot{"answer5":"yes"}
    - action_answer5_submit
    - utter_question_6
    
* said_no
    - slot{"answer6":"no"}
    - action_answer6_submit
    - utter_8

## story 9
> Check_question3

* said_yes
    - slot{"answer3":"yes"}
    - action_answer3_submit
    - utter_question_4
    
* said_yes
    - slot{"answer4":"yes"}
    - action_answer4_submit
    - utter_question_5
    
* said_yes
    - slot{"answer5":"yes"}
    - action_answer5_submit
    - utter_question_6
    
* said_yes
    - slot{"answer6":"yes"}
    - action_answer6_submit
    - utter_9







<!-- 
## story 2

* greet
    - utter_greet
    - slot{"name":"Rahul"}
* saidname{"name":"Rahul"}
    - slot{"name":"Rahul"}
    - utter_sayname
* procurement
    - utter_question_1
* said_yes
    - utter_question_2
* said_no
    - utter_question_3
* said_yes
    - utter_question_4
* said_no
    - utter_question_5
* said_no
    - utter_question_6
* said_no
    - utter_2

## story 3

* greet
    - utter_greet
    - slot{"name":"Rahul"}
* saidname{"name":"Rahul"}
    - slot{"name":"Rahul"}
    - utter_sayname
* procurement
    - utter_question_1
* said_yes
    - utter_question_2
* said_no
    - utter_question_3
* said_yes
    - utter_question_4
* said_no
    - utter_question_5
* said_no
    - utter_question_6
* said_yes
    - utter_3

## story 4

* greet
    - utter_greet
    - slot{"name":"Rahul"}
* saidname{"name":"Rahul"}
    - slot{"name":"Rahul"}
    - utter_sayname
* procurement
    - utter_question_1
* said_yes
    - utter_question_2
* said_no
    - utter_question_3
* said_yes
    - utter_question_4
* said_no
    - utter_question_5
* said_yes
    - utter_question_6
* said_no
    - utter_4
    
## story 5

* greet
    - utter_greet
    - slot{"name":"Rahul"}
* saidname{"name":"Rahul"}
    - slot{"name":"Rahul"}
    - utter_sayname
* procurement
    - utter_question_1
* said_yes
    - utter_question_2
* said_no
    - utter_question_3
* said_yes
    - utter_question_4
* said_no
    - utter_question_5
* said_yes
    - utter_question_6
* said_yes
    - utter_5
    
## story 6

* greet
    - utter_greet
    - slot{"name":"Rahul"}
* saidname{"name":"Rahul"}
    - slot{"name":"Rahul"}
    - utter_sayname
* procurement
    - utter_question_1
* said_yes
    - utter_question_2
* said_no
    - utter_question_3
* said_yes
    - utter_question_4
* said_yes
    - utter_question_5
* said_no
    - utter_question_6
* said_no
    - utter_6
    
## story 7

* greet
    - utter_greet
    - slot{"name":"Rahul"}
* saidname{"name":"Rahul"}
    - slot{"name":"Rahul"}
    - utter_sayname
* procurement
    - utter_question_1
* said_yes
    - utter_question_2
* said_no
    - utter_question_3
* said_yes
    - utter_question_4
* said_yes
    - utter_question_5
* said_no
    - utter_question_6
* said_yes
    - utter_7
    
## story 8

* greet
    - utter_greet
    - slot{"name":"Rahul"}
* saidname{"name":"Rahul"}
    - slot{"name":"Rahul"}
    - utter_sayname
* procurement
    - utter_question_1
* said_yes
    - utter_question_2
* said_no
    - utter_question_3
* said_yes
    - utter_question_4
* said_yes
    - utter_question_5
* said_yes
    - utter_question_6
* said_no
    - utter_8
    
## story 9

* greet
    - utter_greet
    - slot{"name":"Rahul"}
* saidname{"name":"Rahul"}
    - slot{"name":"Rahul"}
    - utter_sayname
* procurement
    - utter_question_1
* said_yes
    - utter_question_2
* said_no
    - utter_question_3
* said_yes
    - utter_question_4
* said_yes
    - utter_question_5
* said_yes
    - utter_question_6
* said_yes
    - utter_9 -->