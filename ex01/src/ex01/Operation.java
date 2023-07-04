package ex01;

public class Operation {

	public static void run() {
		// 산술연산자
		int kor = 40;
		int eng = 88;
		int mat = 76;
		int sum = kor + eng + mat;
		double avg = sum / 3.;

		System.out.printf("국어:" + "%d" + "점\n", kor);
		System.out.printf("영어:" + "%d" + "점\n", eng);
		System.out.printf("수학:" + "%d" + "점\n", mat);
		System.out.printf("총합:" + "%d" + "점\n", sum);
		System.out.printf("평균:" + "%.2f" + "점\n", avg);

		// 관계연산자

		// 삼항연산자
		String pass = kor >= 60 && eng >= 60 && mat >= 60 && avg >= 70 ? "합격" : "불합격";
		System.out.println("결과:" + pass);

		int count = 0;
		if (kor < 60) count++;
		if (eng < 60) count++;
		if (mat < 60) count++;
		System.out.print("누락과목수:"+count);
	

	}

}
