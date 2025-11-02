#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m; // n = processes, m = resources
    cout << "Enter the no. of processes: ";
    cin >> n;
    cout << "Enter the no. of resources: ";
    cin >> m;

    vector<vector<int>> maxNeed(n, vector<int>(m));
    vector<vector<int>> alloc(n, vector<int>(m));
    vector<vector<int>> need(n, vector<int>(m));
    vector<int> avail(m);

    // Input maximum and allocation for each process
    for (int i = 0; i < n; i++) {
        cout << "\nProcess " << i + 1 << endl;
        for (int j = 0; j < m; j++) {
            cout << "Maximum value for resource " << j + 1 << ": ";
            cin >> maxNeed[i][j];
        }
        for (int j = 0; j < m; j++) {
            cout << "Allocated from resource " << j + 1 << ": ";
            cin >> alloc[i][j];
        }
    }

    cout << "\n";
    for (int j = 0; j < m; j++) {
        cout << "Enter total value of resource " << j + 1 << ": ";
        cin >> avail[j];
    }

    // Calculate the available vector
    for (int j = 0; j < m; j++) {
        int sum = 0;
        for (int i = 0; i < n; i++)
            sum += alloc[i][j];
        avail[j] -= sum;
    }

    // Calculate the need matrix
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            need[i][j] = maxNeed[i][j] - alloc[i][j];

    vector<bool> finish(n, false);
    vector<int> safeSeq;
    int count = 0;

    while (count < n) {
        bool found = false;
        for (int i = 0; i < n; i++) {
            if (!finish[i]) {
                bool possible = true;
                for (int j = 0; j < m; j++) {
                    if (need[i][j] > avail[j]) {
                        possible = false;
                        break;
                    }
                }

                if (possible) {
                    for (int j = 0; j < m; j++)
                        avail[j] += alloc[i][j];
                    safeSeq.push_back(i);
                    finish[i] = true;
                    found = true;
                    count++;
                }
            }
        }

        if (!found) {
            cout << "\nThe System is not in a safe state.\n";
            return 0;
        }
    }

    cout << "\nProgram Output:\n";
    cout << "The System is currently in safe state and\n< ";
    for (int i = 0; i < n; i++)
        cout << "P" << safeSeq[i] + 1 << (i == n - 1 ? " " : " ");
    cout << "> is the safe sequence.\n";

    return 0;
}
