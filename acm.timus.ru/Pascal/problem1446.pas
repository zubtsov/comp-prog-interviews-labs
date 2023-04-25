program problem1446;
type
        mPoint = ^mas;
        mas = record
                student:string[200];
                N:mPoint;
        end;
var
        slytherin, hufflepuff, gryffindor, ravenclaw:mPoint;
        sF, hF, gF, rF:mPoint;

        k,i:integer;

procedure add_elem(var fac:mPoint; stud:string);
var
        last:mPoint;
begin
        New(last);
        fac^.student:=stud;
        fac^.N:=last;
        fac:=last;
        fac^.N:=nil
end;

procedure fill_data();
var
        stud:string[200];
        fac:string[20];
begin
        readln(stud);
        readln(fac);
        case fac[1] of
                'G':add_elem(gryffindor,stud);
                'H':add_elem(hufflepuff,stud);
                'S':add_elem(slytherin,stud);
                'R':add_elem(ravenclaw,stud);
        end;
end;

procedure write_fac(current:mPoint);
begin
        if (current^.N <> nil) then begin
                writeln(current^.student);
                write_fac(current^.N)
        end
end;

begin
        New(gryffindor);New(hufflepuff);New(slytherin);New(ravenclaw);
        New(sF);New(hF);New(gF);New(rF);

        sF^.N:=slytherin;
        sF^.student:='Slytherin:';
        hF^.N:=hufflepuff;
        hF^.student:='Hufflepuff:';
        gF^.N:=gryffindor;
        gF^.student:='Gryffindor:';
        rF^.N:=ravenclaw;
        rF^.student:='Ravenclaw:';

        readln(k);
        for i:=1 to k do
                fill_data();

        write_fac(sF);
        writeln();
        write_fac(hF);
        writeln();
        write_fac(gF);
        writeln();
        write_fac(rF)
end.