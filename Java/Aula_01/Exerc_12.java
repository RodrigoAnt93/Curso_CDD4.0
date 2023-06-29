package aula_1;

import java.util.Scanner;

public class Exerc_12 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		int a = sc.nextInt();
		System.out.print("Digite outro numero: ");
		int b = sc.nextInt();
		System.out.print("Digite outro numero: ");
		int c = sc.nextInt();
		
		if (a > b && b > c) {
			System.out.println("A");
		}
		else {
			if (b > c) {
				System.out.println("B");
			}
			else {
				System.out.println("C");
			}
		}
		
		if (a < b && b < c) {
			System.out.println("A");
		}
		else {
			if (b < c) {
				System.out.println("B");
			}
			else {
				System.out.println("C");
			}
		}
		sc.close();
	}

}
