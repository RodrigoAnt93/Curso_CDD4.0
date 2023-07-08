package fundamentos;

import java.util.Scanner;

public class Exerc_06 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		double nota[] = new double[5];
		
		for (int i=0; i < nota.length; i++) {
			System.out.print("Digite a " + (i + 1) + "° nota: ");
			double n = sc.nextDouble();
			nota[i] = n;
		}
		double media = 0;
		for (int i=0; i < nota.length; i++) {
			media += nota[i];
		}
		System.out.println();
		System.out.println("A média é: " + media / nota.length);

	}

}
