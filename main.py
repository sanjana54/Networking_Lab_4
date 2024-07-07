import matplotlib.pyplot as plt

def bresenham_line(point1, point2):
    print('Points are: ', point1, point2)
    x1, y1 = point1
    x2, y2 = point2
    all_points = []
    all_p = []
    dy = y2 - y1
    dx = x2 - x1
    if dy < dx:
        print('Slope is lesser than one')
        x, y = x1, y1
        p = 2 * dy - dx

        while x <= x2:
            all_points.append((x, y))
            all_p.append(p)
            x += 1
            if p < 0:
                p = p + 2 * dy
            else:
                p = p + 2 * dy - 2 * dx
                y += 1
        
    else:
        print('Slope is greater or equal to one')
        p = 2 * dx - dy
        x, y = x1, y1
        while y <= y2:
            all_points.append((x, y))
            all_p.append(p)
            y += 1
            if p < 0:
                p = p + 2 * dx
            else:
                p = p + 2 * dx - 2 * dy
                x += 1
    
    print("Intermediate Points are: ", all_points)
    print("Decision Parameters are: ", all_p)

    # visual Representations

    x_coord = [coord[0] for coord in all_points]
    y_coord = [coord[1] for coord in all_points]
    plt.plot(x_coord, y_coord, marker='o', color='blue')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"Line Between {point1} and {point2}")
    plt.grid(True)
    plt.show()

def main():
    print('\nBresenham Line Drawing Algorithm')
    # Test Purpose
    point1 = [1, 1]
    point2 = [8, 4]
    bresenham_line(point1, point2)

    point1 = [1, 1]
    point2 = [4, 8]
    bresenham_line(point1, point2)



if __name__ == "__main__":
    main()