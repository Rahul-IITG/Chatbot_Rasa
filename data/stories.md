## story greet

* greet
    - utter_greet
    - utter_howhelp
> check_greet

## story 99_start

> check_greet
* notspend_funds
- utter_confirm_99
> check_99

## story 99_end1

> check_99
* said_no
- utter_99


## story 0_1

> check_greet
* procurement OR spend_funds
- utter_question_2
* said_yes
- utter_0

## story 0_2

> check_greet
* procurement OR spend_funds
- utter_question_2
* less_5000
- utter_0

## story 0_3

> check_greet
* less_5000
- utter_0

## story 1_start1

> check_greet
* procurement OR spend_funds
- utter_question_2
* said_no
- utter_question_3
> check_question3

## story 1_start2

> check_greet
* procurement OR spend_funds
- utter_question_2
* more_5000
- utter_question_3
> check_question3

## story 1_end1

> check_question3
* said_no
- utter_1

## story 1_end2

> check_question3
* dont_know_supplier
- utter_1

## story 1_direct

> check_greet
* dont_know_supplier
- utter_1

## story 2_1

> check_question3
* said_yes OR know_supplier
- utter_question_4
> check_question4
* said_no OR not_supplierofmc
- utter_question_5
* said_no
- utter_question_6
* said_no OR notdiscussed_price
- utter_2

## story 2_2

> check_greet
* know_supplier
- utter_question_4
* said_no OR not_supplierofmc
- utter_question_5
* said_no
- utter_question_6
* said_no OR notdiscussed_price
- utter_2

## story 2_3

> check_greet
* not_supplierofmc
- utter_question_5
* said_no
- utter_question_6
* said_no OR notdiscussed_price
- utter_2


## story 3_1

> check_question4
* said_no OR not_supplierofmc
- utter_question_5
* said_no
- utter_question_6
* said_yes OR discussed_price
- utter_3


## story 3_2

> check_greet
* not_supplierofmc
- utter_question_5
* said_no
- utter_question_6
* said_yes OR discussed_price
- utter_3


## story 3_3

> check_greet
* know_supplier
- utter_question_4
> check_question4

## story 4_1

> check_question4
* said_no OR not_supplierofmc
- utter_question_5
* said_yes
- utter_question_6
* said_no OR notdiscussed_price
- utter_4

## story 4_2

> check_greet
* not_supplierofmc
- utter_question_5
* said_yes
- utter_question_6
* said_no OR notdiscussed_price
- utter_4

## story 4_3

> check_greet
* know_supplier
- utter_question_4
> check_question4

## story 5_1

> check_question4
* said_no OR not_supplierofmc
- utter_question_5
* said_yes
- utter_question_6
* said_yes OR discussed_price
- utter_5

## story 5_2

> check_greet
* not_supplierofmc
- utter_question_5
* said_yes
- utter_question_6
* said_yes OR discussed_price
- utter_5

## story 5_3

> check_greet
* know_supplier
- utter_question_4
> check_question4

## story 6_1

> check_question4
* said_yes OR supplierofmc
- utter_question_5
* said_no
- utter_question_6
* said_no OR notdiscussed_price
- slot{"output":"6"}
- action_database
- utter_6

## story 6_2

> check_greet
* know_supplier
- utter_question_4
> check_question4

## story 6_3

> check_greet
* supplierofmc
- utter_question_5
* said_no
- utter_question_6
* said_no OR notdiscussed_price
- utter_6

## story 7_1

> check_question4
* said_yes OR supplierofmc
- utter_question_5
* said_no
- utter_question_6
* said_yes OR discussed_price
- utter_7

## story 7_2

> check_greet
* know_supplier
- utter_question_4
> check_question4

## story 7_3

> check_greet
* supplierofmc
- utter_question_5
* said_no
- utter_question_6
* said_yes OR discussed_price
- utter_7


## story 8_1

> check_question4
* said_yes OR supplierofmc
- utter_question_5
* said_yes
- utter_question_6
* said_no OR notdiscussed_price
- utter_8

## story 8_2

> check_greet
* know_supplier
- utter_question_4
> check_question4

## story 8_3

> check_greet
* supplierofmc
- utter_question_5
* said_yes
- utter_question_6
* said_no OR notdiscussed_price
- utter_8


## story 9_1

> check_question4
* said_yes OR supplierofmc
- utter_question_5
* said_yes
- utter_question_6
* said_yes OR discussed_price
- utter_9

## story 9_2

> check_greet
* know_supplier
- utter_question_4
> check_question4

## story 9_3

> check_greet
* supplierofmc
- utter_question_5
* said_yes
- utter_question_6
* said_yes OR discussed_price
- utter_9

<!---
## story fallback

* greet OR said_yes OR said_no OR know_supplier OR procurement OR supplierofmc OR not_supplierofmc OR discussed_price OR notdiscussed_price
- custom_fallback_action
--->