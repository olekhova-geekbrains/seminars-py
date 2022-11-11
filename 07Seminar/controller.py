import view
import model


def my_func() -> list:
    num1 = model.parsing(view.data_in())
    num2 = model.parsing(view.data_in())
    oper = view.data_op()
    result = model.calculate(num1, num2, oper)
    return view.show_data(result)


if __name__ == "__main__":
    my_func()
