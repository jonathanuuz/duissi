def approve(request, project_id, location, key_ring_id, key_id):
    """
    Approve a pending key.

    Args:
        project_id (string): Google Cloud project ID (e.g. 'my-project').
        location (string): Cloud KMS location (e.g. 'us-east1').
        key_ring_id (string): ID of the Cloud KMS key ring (e.g. 'my-key-ring').
        key_id (string): ID of the key to use (e.g. 'my-key').

    Returns:
        CryptoKey: Cloud KMS key.

    """

    # Import the client library.
    from google.cloud import kms

    # Import time for sleep.
    import time

    # Create the client.
    client = kms.KeyManagementServiceClient()

    # Build the key name.
    key_name = client.crypto_key_path(project_id, location, key_ring_id, key_id)

    # Call the API.
    approved_key = client.update_crypto_key_primary_version(
        request={'name': key_name, 'crypto_key_version_id': '1'}
    )
    print('Approved key: {}'.format(approved_key.name))
    return approved_key

  
