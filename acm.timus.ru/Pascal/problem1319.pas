program problem1319;
var
        i,j,k,t,N:word;
begin
        readln(N);
        k:=1+(N*(N-1) div 2);
        for i:=N downto 1 do begin
                t:=k;
                write(t,' ');
                {выводим i-ю строку}

                for j:=i to N-1 do begin
                        t:=t-j;
                        write(t,' ');
                end;

                for j:=N-1 downto N-(i-1) do begin
                        t:=t-j;
                        write(t,' ');
                end;
                k:=k+i;
                writeln()
        end;

end.