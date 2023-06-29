package aula_1;

import java.util.Scanner;

public class Exerc_9 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		int resp = sc.nextInt();
		
		if (resp != 0) {
			if(resp > 0) {
			System.out.println("POSITIVO!");
		}
		else {
			System.out.println("NEGATIVO!");
		}}
		else {
			System.out.println("NEUTRO.");
		}
		sc.close();

	}

}
