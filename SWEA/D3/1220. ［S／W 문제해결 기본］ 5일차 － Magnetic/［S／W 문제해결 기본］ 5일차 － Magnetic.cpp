#include<iostream>

using namespace std;

int table[100][100], lock_cnt;

void move() {
    for (int i=0; i<100; i++) {
        for (int j=0; j<100; j++) {
            if (table[i][j] == 1) {
                if (i+1 < 100) {
                    if (table[i+1][j] == 0) {
                        table[i][j] = 0;
                        table[i+1][j] = 1;
                    } else if (table[i+1][j] == 2) {
                        lock_cnt++;
                    }
                } else table[i][j] = 0;
            } 
        }
    }

    for (int i=99; i<=0; i--) {
        for (int j=0; j<100; j++) {
            if (table[i][j] == 2) {
                if (i-1 >= 0) {
                    if (table[i-1][j] == 0) {
                        table[i][j] = 0;
                        table[i-1][j] = 1;
                    } else if (table[i-1][j] == 1) {
                        lock_cnt++;
                    }
                } else table[i][j] = 0;
            } 
        }
    }
}

int main(int argc, char** argv)
{
	int test_case;
	int T = 10;

	for(test_case = 1; test_case <= T; ++test_case)
	{
        lock_cnt = 0;
        int N;
        cin >> N;
        for (int i=0;i<N;i++) {
            for (int j=0;j<N;j++) {
                int n;
                cin >> n;
                table[i][j] = n;
            }
        }
        move();
        cout << "#" << test_case << " " << lock_cnt << endl;
	}
	return 0;
}
