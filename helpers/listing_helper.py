from data import BASE_LISTING_PAYLOAD


def create_listing(listing_client, token):
    response = listing_client.create_listing(token, BASE_LISTING_PAYLOAD)
    return response.json()


def delete_all_user_listings(listing_client, token):
    response = listing_client.get_own_listings(token)
    for listing in response.json()['offers']:
        listing_client.delete_listing(token, listing['id'])


def delete_listing(listing_client, token, listing_id):
    listing_client.delete_listing(token, listing_id)
