package aula_3;

import java.util.Scanner;

public class Exerc_05 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Digite um texto: ");
		String txt = sc.nextLine();
		System.out.println(txt.toUpperCase());
		
		sc.close();

	}

}
