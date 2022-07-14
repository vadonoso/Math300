A = [2 -1 4;9 6 2;1 3 8];
B = [1 1 1;1 1 1;1 1 1];
x = [3;6;8];
y = [5 10 15];

ans1 = A * B;
ans2 = A * x;
ans3 = x' * B;
ans4 = B * y;
ans5 = x * A;
ans6 = x * y;
ans7 = y * x;
ans8 = x * y';
ans9 = x.*y;
ans10 = A.*B;