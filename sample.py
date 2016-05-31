from node import node

SIMPLE = node(
        data=1,
        down=node(
            data=2,
            down=None,
            right=None
        ),
        right=node(
            data=3,
            down=None,
            right=None
        )
    )

COMPLEX = node(
        1,
        down=node(
            2,
            down=node(
                3,
                down=None,
                right=None
            ),
            right=node(
                4,
                down=None,
                right=None
            )
        ),
        right=node(
            5,
            down=None,
            right=node(
                6,
                down=node(
                    7,
                    down=node(8,
                        None,
                        None
                    ),
                    right=node(
                        9,
                        down=None,
                        right=node(
                            10,
                            None,
                            None
                        )
                    )
                ),
                right=None
            )
        )
    )

