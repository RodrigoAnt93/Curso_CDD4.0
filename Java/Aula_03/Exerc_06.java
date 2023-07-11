package aula_3;

import java.util.Arrays;

public class Exerc_06 {

	public static void main(String[] args) {
		String[] txt = {"a", "vida", "é", "bela"};
		String txt2 = "";
		for(String c : txt) {
			txt2 += (c + " ");
		}
		System.out.println(txt2.toUpperCase());
		
		String txt3 = "";
		for(int i = (txt.length - 1); i >= 0; i--) {
			txt3 += (txt[i] + " ");
		}
		System.out.println(txt3.toUpperCase());

	}

}
