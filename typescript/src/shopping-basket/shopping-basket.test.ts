type Item = { name: string; price: number };
function createBasket() {
  const items: Item[] = [];
  return {
    add: (item: Item) => items.push(item),
    addMany: (item: Item, quantity: number) => {
      const addedItems: Item[] = Array.from({ length: quantity }, () => ({
        ...item,
      }));
      items.push(...addedItems);
    },
    count: (item: Item) =>
      items.filter((i) => i.name === item.name)?.length || 0,
    totalPrice: () => {
      const totalPrice = items
        .map((item) => item.price)
        .reduce((totalPrice, price) => totalPrice + price, 0);
      if (totalPrice > 200) return totalPrice * (1 - 10 / 100);
      else if (totalPrice > 100) return totalPrice * (1 - 5 / 100);
      return totalPrice;
    },
  };
}

describe("shopping basket", () => {
  it("returns the quantity of a basket containing a single item", () => {
    let item = {
      name: "Item",
      price: 10,
    };
    let basket = createBasket();
    basket.add(item);

    let quantityOfItem = basket.count(item);
    expect(quantityOfItem).toBe(1);
  });

  it("returns the quantity of a basket containing multiple equal items", () => {
    let item = {
      name: "Item",
      price: 10,
    };
    let item2 = {
      name: "Item",
      price: 20,
    };
    let basket = createBasket();
    basket.add(item);
    basket.add(item2);

    let quantityOfItem = basket.count(item);
    expect(quantityOfItem).toBe(2);
  });

  it("returns the quantity of a basket containing different items", () => {
    let item = {
      name: "Item",
      price: 10,
    };
    let banana = {
      name: "Banana",
      price: 20,
    };
    let basket = createBasket();
    basket.add(item);
    basket.add(banana);

    let quantityOfItem = basket.count(item);
    expect(quantityOfItem).toBe(1);
  });

  it("calculates the total price of a basket with a single item", () => {
    let item = {
      name: "Item",
      price: 10,
    };
    let basket = createBasket();
    basket.add(item);

    let totalBasketPrice = basket.totalPrice();
    expect(totalBasketPrice).toBe(10);
  });

  it("calculates the total price of a basket with multiple items", () => {
    let item = {
      name: "Item",
      price: 10,
    };
    let banana = {
      name: "Banana",
      price: 20,
    };
    let basket = createBasket();
    basket.add(item);
    basket.add(banana);

    let totalBasketPrice = basket.totalPrice();
    expect(totalBasketPrice).toBe(30);
  });

  it("applies a 5% discount to the total price if the value of the basket is bigger than 100", () => {
    let banana = {
      name: "Banana",
      price: 20,
    };
    let basket = createBasket();
    basket.addMany(banana, 6);

    let totalBasketPrice = basket.totalPrice();
    expect(totalBasketPrice).toBe(114);
  });

  it("applies a 10% discount to the total price if the value of the basket is bigger than 200", () => {
    let banana = {
      name: "Banana",
      price: 20,
    };
    let basket = createBasket();
    basket.addMany(banana, 11);

    let totalBasketPrice = basket.totalPrice();
    expect(totalBasketPrice).toBe(198);
  });
});
