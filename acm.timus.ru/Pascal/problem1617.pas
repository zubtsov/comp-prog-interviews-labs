program problem1617;
var
        n,i,d,count:integer;
        a:array[600..700] of byte;
begin
        readln(n);
        count:=0;
        for i:=600 to 700 do a[i]:=0;

        for i:=1 to n do begin
                readln(d);
                inc(a[d]);
        end;
        for i:=600 to 700 do
                if (a[i]>3) then
                        inc(count, a[i] div 4);
        writeln(count);
end.
