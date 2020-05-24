## story start
* start
- action_session_start

## story greet

* greet
- utter_howhelp
> check_greet

## story 99_start

> check_greet
* notspend_funds
- utter_confirm_99
> check_99

## story 99_end1

> check_99
* said_no OR notspend_funds
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
* said_no OR dont_know_supplier
- utter_1
- utter_help_supplier_selection
> check_1_continue

## story 1_end2

> check_question3
* dont_know_supplier
- utter_1
- utter_help_supplier_selection
> check_1_continue

## story 1_direct

> check_greet
* dont_know_supplier
- utter_1
- utter_help_supplier_selection
> check_1_continue

## story 1 continue1

> check_1_continue
* said_yes OR know_supplier
- utter_provide_supplier
- action_listen
* freetext
- utter_list_questions1_1
* said_yes OR said_no
- utter_list_questions1_2
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_triage

## story 1 continue2

> check_1_continue
* said_no OR dont_know_supplier
- utter_list_questions1_1
* said_yes OR said_no
- utter_list_questions1_2
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_triage

## story 2_1

> check_question3
* said_yes OR know_supplier
- utter_assess_other_supplier
- action_listen
* said_no
- utter_question_4
> check_question4
* said_no OR not_supplierofmc
- utter_question_5
> check_question_5
* said_no OR not_clear_description
- utter_question_6
* said_no OR notdiscussed_price
- utter_2
- utter_confirmation
> check_confirm2
* said_yes
- utter_list_question2_1
> check_2_continue

## story 2_1_2

> check_question3
* said_yes OR know_supplier
- utter_assess_other_supplier
- action_listen
* said_yes
- utter_provide_supplier
- action_listen
* freetext
- utter_list_questions1_1
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_list_questions1_2
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_triage

## story 1 continue1

> check_1_continue
- utter_provide_supplier
- action_listen
* freetext
- utter_list_questions1_1
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_list_questions1_2
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_triage

## story 2_2

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_no
- utter_question_4
* said_no OR not_supplierofmc
- utter_question_5
* said_no OR not_clear_description
- utter_question_6
* said_no OR notdiscussed_price
- utter_2
- utter_confirmation
> check_confirm2
* said_yes
- utter_list_question2_1
> check_2_continue

## story 2_2_2

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_yes
- utter_provide_supplier
- action_listen
* freetext
- utter_list_questions1_1
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_list_questions1_2
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_triage

## story 2_3

> check_greet
* not_supplierofmc

- utter_question_5
* said_no OR not_clear_description
- utter_question_6
* said_no OR notdiscussed_price
- utter_2
- utter_confirmation

> check_confirm2
* said_yes
- utter_list_question2_1
> check_2_continue

## story 2_continue1
> check_2_continue
* said_yes OR know_supplier
- utter_ask_sourcing_rep
- action_listen
* freetext
- utter_2

## story 2_continue2
> check_2_continue
* said_no OR dont_know_supplier
- utter_triage

## story wrong2
> check_confirm2
* said_no
- utter_wrong

## story 3_1

> check_question4
* said_no OR not_supplierofmc

- utter_question_5
* said_no OR not_clear_description
- utter_question_6
* said_yes OR discussed_price
- utter_3
- utter_confirmation

> check_confirm3
* said_yes
- utter_list_question3_1
- action_listen
* freetext
- utter_list_question3_2
> check_3_continue

## story 3_2

> check_greet
* not_supplierofmc

- utter_question_5
* said_no OR not_clear_description
- utter_question_6
* said_yes OR discussed_price
- utter_3
- utter_confirmation

> check_confirm3
* said_yes
- utter_list_question3_1
- action_listen
* freetext
- utter_list_question3_2
> check_3_continue

## story 3_3

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_no
- utter_question_4
> check_question4

## story 3_3_2

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_yes
> check_1_continue

## story 3_continue1
> check_3_continue
* said_yes OR know_sourcing_rep
- utter_ask_sourcing_rep
- action_listen
* freetext
- utter_3

## story wrong3

> check_confirm3
* said_no
- utter_wrong

## story 3_continue2
> check_3_continue
* said_no OR dont_know_sourcing_rep
- utter_triage

## story 1 continue1

> check_1_continue
- utter_provide_supplier
- action_listen
* freetext
- utter_list_questions1_1
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_list_questions1_2
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_triage


## story 4_1 and 5_1 start

> check_question_5
* said_yes OR clear_description
- utter_list_question4_1
- utter_list_question4_2
- utter_list_question4_3
- utter_list_question4_4
- utter_list_question4_5
- utter_list_question4_6
- action_listen
* said_no
- utter_question_6
> check_4_5

## story 4 end
> check_4_5

* said_no OR notdiscussed_price
- utter_4
- utter_confirmation
<!-- > check_confirm45 -->
* said_yes
- utter_list_question3_2
> check_4_continue

## story 5 end
> check_4_5
* said_yes OR discussed_price
- utter_5
- utter_confirmation

<!-- > check_confirm45 -->
* said_yes
> check_5_continue

<!-- ## story wrong_45

> check_confirm45
* said_no
- utter_wrong -->

## story 4_1_2 and 5_1_2

> check_question4
* said_no OR not_supplierofmc
- utter_question_5
* said_yes OR clear_description
- utter_list_question4_1
- utter_list_question4_2
- utter_list_question4_3
- utter_list_question4_4
- utter_list_question4_5
- utter_list_question4_6
- action_listen
* said_yes
- utter_explain_page1

## story 4_3 and 5_3

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_no
- utter_question_4
> check_question4

## story 4_3_2 and 5_3_2

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_yes
> check_1_continue

## story 1 continue1

> check_1_continue
- utter_provide_supplier
- action_listen
* freetext
- utter_list_questions1_1
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_list_questions1_2
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_triage

## story 4_2 and 5_2 start

> check_greet
* not_supplierofmc
- utter_question_5
* said_yes OR clear_description
- utter_list_question4_1
- utter_list_question4_2
- utter_list_question4_3
- utter_list_question4_4
- utter_list_question4_5
- utter_list_question4_6
- action_listen
* said_no
- utter_question_6
> check_4_5

## story 4_2_2 and 5_2_2

> check_greet
* not_supplierofmc
- utter_question_5
* said_yes OR clear_description
- utter_list_question4_1
- utter_list_question4_2
- utter_list_question4_3
- utter_list_question4_4
- utter_list_question4_5
- utter_list_question4_6
- action_listen
* said_yes
- utter_explain_page1


## story 4_continue1
> check_4_continue
* said_yes OR know_sourcing_rep
- utter_ask_sourcing_rep
- action_listen
* freetext
- utter_4

## story 4_continue2
> check_4_continue
* said_no OR dont_know_sourcing_rep
- utter_triage


## story 5_continue1
> check_5_continue
- utter_list_question9_1
- action_listen
* said_yes OR know_sourcing_rep
- utter_list_question9_2
* freetext
- utter_list_question3_1
* freetext
- utter_triage

## story 5_continue2
> check_5_continue
- utter_list_question9_1
- action_listen
* said_no OR dont_know_sourcing_rep
- utter_list_question3_1
* freetext
- utter_triage

## story 6_1

> check_question3
* said_yes OR know_supplier
- utter_assess_other_supplier
- action_listen
* said_no
- utter_question_4
> check_question4_2
* said_yes OR supplierofmc
- utter_question_5
* said_no OR not_clear_description
- utter_question_6
* said_no OR notdiscussed_price
- utter_6
- utter_confirmation
> check_confirm6
* said_yes
- utter_triage

## story 6_1_2

> check_question3
* said_yes OR know_supplier
- utter_assess_other_supplier
- action_listen
* said_yes
> check_1_continue

- utter_provide_supplier
- action_listen
* freetext
- utter_list_questions1_1
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_list_questions1_2
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_triage

## story 6_2

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_no
- utter_question_4
* said_yes OR supplierofmc
- utter_question_5
* said_no OR not_clear_description
- utter_question_6
* said_no OR notdiscussed_price
- utter_6
- utter_confirmation
> check_confirm6
* said_yes
- utter_triage

## story 6_2_2

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_yes
- utter_provide_supplier
- action_listen
* freetext
- utter_list_questions1_1
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_list_questions1_2
* said_yes OR said_no OR clear_description OR not_clear_description
- utter_triage

## story 6_3

> check_greet
* supplierofmc
- utter_question_5
* said_no OR not_clear_description
- utter_question_6
* said_no OR notdiscussed_price
- utter_6
- utter_confirmation
> check_confirm6
* said_yes
- utter_triage

## story wrong_6

> check_confirm6
* said_no
- utter_wrong


## story 7_1

> check_question4_2
* said_yes OR supplierofmc
- utter_question_5
* said_no OR not_clear_description
- utter_question_6
* said_yes OR discussed_price
- utter_7
- utter_confirmation
> check_confirm7
* said_yes
- utter_triage

## story 7_2

> check_greet
* supplierofmc
- utter_question_5
* said_no OR not_clear_description
- utter_question_6
* said_yes OR discussed_price
- utter_7
- utter_confirmation
> check_confirm7
* said_yes
- utter_triage

## story wrong_7
> check_confirm7
* said_no
- utter_wrong

## story 7_3

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_no
- utter_question_4
> check_question4_2

## story 7_3_2

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_yes
> check_1_continue



## story 89_1

> check_question4_2
* said_yes OR supplierofmc
- utter_question_5
* said_yes OR clear_description
- utter_list_question8_1
- utter_list_question8_2
- utter_list_question8_3
- utter_list_question8_4
- utter_list_question8_5
- utter_list_question8_6
- action_listen
* said_no
- utter_question_6
> check_8_9

## story 89_1_2

> check_question4_2
* said_yes OR supplierofmc
- utter_question_5
* said_yes OR clear_description
- utter_list_question8_1
- utter_list_question8_2
- utter_list_question8_3
- utter_list_question8_4
- utter_list_question8_5
- utter_list_question8_6
- action_listen
* said_yes
- utter_explain_page1



## story 8 end
> check_8_9

* said_no OR notdiscussed_price
- utter_8
- utter_confirmation
- action_listen
<!-- > check_confirm_8_9 -->
* said_yes
- utter_list_question3_2
> check_8_continue



## story 8_continue1
> check_8_continue
* said_yes OR know_sourcing_rep
- utter_ask_sourcing_rep
- action_listen
* freetext
- utter_8

## story 8_continue2
> check_8_continue
* said_no OR dont_know_sourcing_rep
- utter_triage

## story 9 end
> check_8_9

* said_yes OR discussed_price
- utter_9
- utter_confirmation
- action_listen
<!-- > check_confirm_8_9 -->
* said_yes
- utter_list_question9_1
- action_listen
> check_9_continue


## story 9_continue1
> check_9_continue

* said_yes OR know_sourcing_rep
- utter_list_question9_2
* freetext
- utter_coupa

## story 9_continue2
> check_9_continue

* said_no OR dont_know_sourcing_rep
- utter_list_question3_1
* freetext
- utter_coupa



<!-- 
## story wrong_8_9
> check_confirm_8_9
* said_no
- utter_wrong -->


## story 89_2

> check_greet
* supplierofmc
- utter_question_5
* said_yes OR clear_description
- utter_list_question8_1
- utter_list_question8_2
- utter_list_question8_3
- utter_list_question8_4
- utter_list_question8_5
- utter_list_question8_6
- action_listen
* said_no
- utter_question_6
> check_8_9


## story 89_2_2

> check_greet
* supplierofmc
- utter_question_5
* said_yes OR clear_description
- utter_list_question8_1
- utter_list_question8_2
- utter_list_question8_3
- utter_list_question8_4
- utter_list_question8_5
- utter_list_question8_6
- action_listen
* said_yes
- utter_explain_page1

## story 89_3

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_no
- utter_question_4
> check_question4_2

## story 89_3_2

> check_greet
* know_supplier
- utter_assess_other_supplier
- action_listen
* said_yes
> check_1_continue


## story unknown
* no_knowledge
- custom_fallback_action