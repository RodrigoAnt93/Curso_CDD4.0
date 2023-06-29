package aula_1;

import java.util.Scanner;

public class Exerc_11 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		int a = sc.nextInt();
		System.out.print("Digite outro numero: ");
		int b = sc.nextInt();
		System.out.print("Digite outro numero: ");
		int c = sc.nextInt();
		
		System.out.println(a > b && a > c ? "A" : b > c ? "B" : "C" );
		System.out.println(a < b && a < c ? "A" : b < c ? "B" : "C" );
		sc.close();

	}

}
