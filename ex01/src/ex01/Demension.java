package ex01;

import java.util.Scanner;

public class Demension {

	public static void run() {
		
		String[] names = new String[22];
		String[] addresses = new String[22];
	
		
		Scanner s = new Scanner(System.in);
		boolean run = true;
		int index = 0;
		
		
		while(run) {
		System.out.println("==================================");
		System.out.println("1.주소등록 2.목록 0.종료");
		System.out.println("선택");
		String menu = s.nextLine();
		
		switch(menu){
		
		case "0" :
			System.out.println("프로그램 종료");
			run = false;
			break;
			
		case "1" :
			System.out.println("주소등록");
			System.out.println("이름>");
			String name = s.nextLine();
			names[index]=name;
			System.out.println("주소>");
			String address = s.nextLine();
			addresses[index]=address;
			index++;
			System.out.println(index+"명 입력완료!");
			break;
		
		case "2" :
			System.out.println("주소목록");
			System.out.println("이름\t주소");
			System.out.printf("");
			break;
			
		default :
			System.out.println("다시선택");
	}
}
}
}