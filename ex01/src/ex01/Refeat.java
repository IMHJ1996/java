package ex01;

import java.util.Scanner;

public class Refeat {
	public static void run() {

		Scanner s = new Scanner(System.in);
		boolean run = true;

		while (run) {
			System.out.println("-------------------------------------------");
			System.out.println("1)100까지 합 | 2)100까지 짝수 합 | 3)100까지 홀수 합 | 0)종료");
			System.out.println("-------------------------------------------");
			String menu = s.nextLine();
			int sum = 0;

			switch (menu) {
			case "0":
				System.out.println("프로그램 종료");
				run = false;
				break;

			case "1":
				for (int i = 1; i <= 100; i++) {
					sum += i;
				}
				System.out.println(sum);

				break;
			case "2":
				for (int i = 1; i <= 100; i++) {
					if (i % 2 == 0)
						sum += i;
				}
				System.out.println(sum);

				break;

			case "3":
				for (int i = 1; i <= 100; i++) {
					if (i % 2 == 1)
						sum += i;
				}
				System.out.println(sum);

				break;
			default:
				System.out.println("다시입력");

			}

		}
	}
}
