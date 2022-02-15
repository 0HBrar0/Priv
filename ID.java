import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Objects;

class info  implements ActionListener{
    JFrame f = new JFrame();
    JPanel p1 = new JPanel(new GridLayout(4,0,10,10));
    final JButton b1 = new JButton("Next");
    JLabel l1 = new JLabel("Name");
    JLabel l2 = new JLabel("Class");
    final JTextField t1 = new JTextField();
    final JComboBox<String> combosec = new JComboBox<>();
    JLabel section = new JLabel("Section");

    String[] standards={"I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"};

    final JComboBox<String> comboclas = new JComboBox<>(standards);



    info(){

        p1.add(l1);
        p1.add(t1);
        p1.add(l2);
        p1.add(comboclas);
        p1.add(section);
        p1.add(combosec);
        p1.add(b1);

        f.add(p1, BorderLayout.CENTER);

        b1.addActionListener(this);
        comboclas.addActionListener(cb);

        f.setVisible(true);

        f.setSize(350,200);

    }

    ActionListener cb = e -> {
        String strclass = (Objects.requireNonNull(comboclas.getSelectedItem())).toString();
        switch (strclass){
            case "XI":
                combosec.removeAllItems();
                System.out.println("+1");
                section.setText("Stream");
                combosec.addItem("Medical");combosec.addItem("Non-Medical");combosec.addItem("Commerce");combosec.addItem("Humanities");

                break;
            case "XII":
                combosec.removeAllItems();
                System.out.println("+2");
                section.setText("Stream");
                combosec.addItem("Medical");combosec.addItem("Non-Medical");combosec.addItem("Commerce");combosec.addItem("Humanities");
                break;
            default:
                combosec.removeAllItems();
                combosec.addItem("A");combosec.addItem("B");combosec.addItem("C");combosec.addItem("D");
                section.setText("Section");
                System.out.println("normal");


        }
    };
    public void actionPerformed(ActionEvent b) {
        String name = t1.getText();
        String standard = (Objects.requireNonNull(comboclas.getSelectedItem())).toString();
        String sec = (Objects.requireNonNull(combosec.getSelectedItem())).toString();
        System.out.println(name);
        System.out.println(standard);
        System.out.println(sec);
    }
}

public class ID {

    public static void main(String[] args) {
        info n = new info();

    }
}
