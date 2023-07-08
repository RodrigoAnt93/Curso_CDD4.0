package fundamentos;

public class Exerc_01 {

	public static void main(String[] args) {
		
		// TODO Auto-generated method stub

		int sum_1 = 0;
		int sum_2 = 0;
		
		for (int i=1; i<=20; i++) {
			if (i % 3 == 0) {
				System.out.println(i + " e um multiplo de 3.");
				sum_1 += i;
				}
			}
			System.out.println("A soma dos multiplos de 3 e: " + sum_1);
			System.out.println();
			
			for (int i=1; i<=20; i++) {
				if (i % 5 == 0) {
					System.out.println(i + " e um multiplo de 5.");
					sum_2 += i;
					}
				}
				System.out.println("A soma dos multiplos de 5 e: " + sum_2);
				System.out.println();
				System.out.println("A soma de todos os multiplos é " + (sum_1 + sum_2));

	}

}
