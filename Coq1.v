Set Implicit Arguments
Require Import Lia.
Require Import Bool.
Require Import List.
Import ListNotations.

(*1*)

Goal forall (X Y : bool),
(X && (negb Y)) || ((negb X) && (negb Y)) || ((negb X) && Y) = negb X || negb Y.
Proof.
intros. destruct X, Y. 
- now reflexivity.
- now reflexivity.
- now reflexivity.
- now reflexivity. 
Qed.

Goal forall ( X Y Z : bool),
negb ((negb X) && Y && Z) && negb (X && Y && (negb Z)) && (X && (negb Y) && Z) = X && (negb Y) && Z.
Proof.
intros. destruct X, Y, Z. 
- now reflexivity.
- now reflexivity.
- now reflexivity.
- now reflexivity.
- now reflexivity.
- now reflexivity.
- now reflexivity.
- now reflexivity.
Qed.
