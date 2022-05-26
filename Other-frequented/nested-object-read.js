const obj = {
    A: {
      B: {
        C: {
          D: {
            E: 2,
          },
        },
      },
    },
  };
  
  console.log(read(obj, "A.B.C.D.E"));
  //Requires nodejs modules