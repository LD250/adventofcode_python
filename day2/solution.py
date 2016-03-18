def main():
    f = open('input.txt')
    content = f.read()
    lines = content.split('\n')
    def paper_for_box(l, w, h):
        sq_meters = [l * w, l * h, h * w] 
        return sum(sq_meters) * 2 + min(sq_meters)

    def ribbon_for_box(dimensions):
        length = sum([a*2 for a in sorted(dimensions)[:2]])
        return length + reduce(lambda x, y: x*y, dimensions, 1)
    s = 0
    r = 0
    for line in lines:
        if line:
            dimensions = [int(d) for d in line.split('x') if d]
            s += paper_for_box(*dimensions)
            r += ribbon_for_box(dimensions)
    print(s)
    print(r)



if __name__ == "__main__":
    main()
