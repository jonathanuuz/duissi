def visualize_field(field):
    """Visualize a 2D field.

    Args:
        field: A 2D numpy array representing the field.
    """

    plt.figure(figsize=(10, 10))
    plt.imshow(field, cmap="jet")
    plt.colorbar()
    plt.show()

