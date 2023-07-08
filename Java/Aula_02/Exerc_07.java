package fundamentos;

public class Exerc_07 {

	public static void main(String[] args) {
		String str = "Hello";
		
		String resultado = str.replace("l", "w");
		System.out.println(resultado);
		
		String str2 = "Hello World";
		resultado = str2.substring(6);
		System.out.println(resultado);
		
		String str3 = " Hello ";
		resultado = str3.trim();
		System.out.println(resultado);
		

	}

}
