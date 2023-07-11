package aula_3;

import java.util.StringTokenizer;

public class Exerc_01 {

	public static void main(String[] args) {
		String s = "abc";
		int tam = s.length();
		System.out.println(tam);
		
		String str = "Hello World World2";
		int pos = str.lastIndexOf("l");
		System.out.println(pos);
		
		String valor = "CDD4.0 - Java";
		
		System.out.println(valor.compareTo("CDD4.0 - Java") == 0 ? true: false);
		System.out.println(valor.compareTo("CDD4.0 - JAVA") == 0 ? true: false);
		System.out.println(valor.compareToIgnoreCase("CDD4.0 - JAVA") == 0 ? true: false);
		
		System.out.println();
		System.out.println(valor.startsWith("Java"));
		System.out.println(valor.startsWith("C"));
		System.out.println(valor.startsWith("DD", 1));
		
		System.out.println();
		
		StringTokenizer exemplo = new StringTokenizer("O mundo não é mais o mesmo mas não iremos desistir nunca");
		System.out.println(exemplo.countTokens());

	}

}
