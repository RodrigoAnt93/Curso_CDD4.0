package fundamentos;

import java.util.Scanner;

public class Exerc_05 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] a = new int [10];
		int[] b = new int [11];
		int[] c = new int [10];
		int[] d = new int [10];
		
		for (int i=0; i < a.length; i++) {
			System.out.print("Valor A: ");
			int n = sc.nextInt();
			a[i] = n;
		}
		System.out.println();
		for (int i=0; i < b.length; i++) {
			System.out.print("Valor B: ");
			int n = sc.nextInt();
			b[i] = n;
		}
		System.out.println();
		for (int i=0; i < c.length; i++) {
			System.out.print("Valor C: ");
			int n = sc.nextInt();
			c[i] = n;
		}
		System.out.println();
		for (int i=0; i < d.length; i++) {
			System.out.print("Valor D: ");
			int n = sc.nextInt();
			d[i] = n;
		}
		System.out.println();
		System.out.print("a) ");
		
		for (int i : a) {
			System.out.print(i + " ");
		}
		System.out.print("\nb) ");
		for (int i : b) {
			System.out.print(i + " ");
		}
		System.out.print("\nc) ");
		
		for (int i : c) {
			System.out.print(i + " ");
		}
		System.out.print("\nd) ");
		for (int i : d) {
			System.out.print(i + " ");
		}
		System.out.println();

	}

}
