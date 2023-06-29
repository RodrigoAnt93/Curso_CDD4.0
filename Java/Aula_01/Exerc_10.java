package aula_1;

import java.util.Scanner;

public class Exerc_10 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite um numero: ");
		int resp = sc.nextInt();
		
		System.out.println(resp == 0 ? "Negativo" : resp > 0 ? "Positivo" : "Negativo");
		sc.close();
	}

}
