program problem1785;
var
        N:word;
begin
        readln(N);
        case N of
                1..4:write('few');
                5..9:write('several');
                10..19:write('pack');
                20..49:write('lots');
                50..99:write('horde');
                100..249:write('throng');
                250..499:write('swarm');
                500..999:write('zounds');
        else
                write('legion');
        end;
end.