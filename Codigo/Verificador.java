
import java.util.Scanner;
import java.util.Stack;

public class Verificador {
    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);
        System.out.print("Digite a expressão: ");
        String expressao = leitor.nextLine();

        Stack<Character> pilha = new Stack<>();
        boolean valido = true;

        for (char c : expressao.toCharArray()) {

            if (c == '(' || c == '[' || c == '{') {
                pilha.push(c);
            }

            if (c == ')' || c == ']' || c == '}') {

                if (pilha.isEmpty()) {
                    valido = false;
                    break;
                }

                char topo = pilha.pop();

                if ((c == ')' && topo != '(') ||
                    (c == ']' && topo != '[') ||
                    (c == '}' && topo != '{')) {
                    valido = false;
                    break;
                }
            }
        }

        if (!pilha.isEmpty()) {
            valido = false;
        }

        if (valido) {
            System.out.println("Expressão válida!");
        } else {
            System.out.println("Expressão inválida!");
        }

        leitor.close();
    }
}



//Daniel Luca 
//323112685

//Hercules Henrique
//322121514
