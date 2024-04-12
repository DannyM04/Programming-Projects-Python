import java.util.Scanner;

public class BankAccount {
    // The following lines compare the user's credentials with the stored credentials and authenticates the user if they're correct. 
    public static class Authentication {
        public static boolean authenticate(String enteredName, int enteredNumber) {
            String correctName = "John Smith";
            int correctNumber = 123456;
            return enteredName.equals(correctName) && enteredNumber == correctNumber;

    }

}
    // The following lines create a navigation menu for the user to use their bank account.
    public static class Menu {
        public static int mainMenu(Scanner scanner) {
            System.out.println("Navigation Menu:");
            System.out.println("1. View Balance");
            System.out.println("2: Deposit");
            System.out.println("3: Withdraw");
            int navigation = scanner.nextInt();
            return navigation;
        }
    }
          
        


    public static void main(String[] args) { 
        Scanner scanner = new Scanner(System.in);
        // The prompt asks the user for their account name and stores it as the variable enteredName
        System.out.println("Please enter your Account Name:");
        String enteredName = scanner.nextLine();
        // The prompt asks the user for their account number and stores it as the variable enteredNumber
        System.out.println("Please enter your Account Number:");
        int enteredNumber = scanner.nextInt();

        // We establish a default balance of £100 for the user
        int defaultBalance = 100;

        boolean Authenticated = Authentication.authenticate(enteredName, enteredNumber);
        // If the account if authenticated, the user recieves the navigation menu. A switch is then made for their responses that carries out each function
        if (Authenticated) {
            String menuResponse;
            do {
                int navigation;
                navigation = Menu.mainMenu(scanner); 
                switch (navigation) {
                    // Case 1 displays the balance of the user
                    case 1:
                        System.out.println("Current Balance : £" + defaultBalance);
                        break;
                    // case 2 prompts the user for how much they wish to deposit. Then confirms that they are depositing more than £0 before completing the deposit
                        case 2:
                        System.out.println("Please enter the amount you wish to deposit:");
                        int depositAmount = scanner.nextInt();
                        if (depositAmount <= 0) {
                            System.out.println("Error: the amount deposited was below or equal to £0");
                        } else {
                            defaultBalance += depositAmount;
                            System.out.println("Success: £" + depositAmount + " has been deposited into your account");
                        }
                        break;                    
                    // case 3 prompts the user on how much they wish to withdraw. Then confirms that they have the sufficiant funds to withdraw and does so. 
                        case 3:
                        System.out.println("Please enter the amount you wish to withdraw:");
                        int withdrawAmount = scanner.nextInt();
                        if (withdrawAmount > defaultBalance) {
                            System.out.println("Error: insufficient funds to withdraw");
                        } else {
                            defaultBalance -= withdrawAmount;
                            System.out.println("Success: £" + withdrawAmount + " has been withdrawn");
                        }
                        break;
                    // any input from the navigation menu that isn't 1-3 is defaulted as an error
                        default:
                        System.out.println("Error: Invalid selection");
                }
                // The following lines asks the user if they wish to return to the navigation menu. If they select yes, it repeats the do-while loop. If not, the program stops.
                System.out.println("Do you wish to return to the Navigation Menu? (yes/no)");
                menuResponse = scanner.next(); // Duplicate local variable menuResponse
            } while (menuResponse.equalsIgnoreCase("yes"));
        } else {
            System.out.println("Error: Authentication failed. Please try again");
        }
        
        scanner.close();
    }

}

