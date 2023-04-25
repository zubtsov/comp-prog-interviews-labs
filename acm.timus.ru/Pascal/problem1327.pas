program  problem1327;
var
        A,B,C:integer;
begin
        readln(A,B);
        if (not odd(A)) then inc(A);
        if (not odd(B)) then dec(B);
        write((B-A) div 2 + 1);
end.
