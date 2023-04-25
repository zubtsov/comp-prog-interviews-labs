program problem1496;
var
        o,s:array[1..100] of string[30];
        n,i,j:integer;
begin
        readln(n);
        for i:=1 to n do begin
                readln(s[i]);
                for j:=1 to i do
                        if (s[j]=s[i]) and (i<>j) then begin
                                s[i]:='';
                                o[j]:=s[j];
                        end
        end;
        for i:=1 to n do
                if(o[i] <> '') then
                        writeln(o[i]);
end.
