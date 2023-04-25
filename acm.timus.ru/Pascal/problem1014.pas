program problem1014;
var
        N,i:longint;
        number,temp:string;
begin
        readln(N);
        case N of
                0:writeln(10);
                1..9:writeln(N);
        else
                i:=9;
                while (N>1) and (i>1) do begin
                        if (N mod i = 0) then begin
                                str(i,temp);
                                number:=temp+number;
                                N:=N div i;
                                i:=9
                        end else
                                i:=i-1
                end;
                if (N>1) then
                        writeln('-1')
                else
                        writeln(number)
        end
end.
