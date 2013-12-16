<?php
namespace DinDin\DinDin\Entities;
/**
 * @Entity @Table(name="users")
 */
class User implements \JsonSerializable
{
    /**
     * @Id @GeneratedValue @Column(type="integer")
     * @var int
     */
    protected $id;

    /**
     * @Column(type="string")
     * @var string
     */
    protected $firstName;

    /**
     * @Column(type="string")
     * @var string
     */
    protected $lastName;

    /**
     * @Column(type="string")
     * @var string
     */
    protected $email;

    /**
     * @ManyToMany(targetEntity="Address")
     * @JoinTable(name="users_addresses",
     *      joinColumns={@JoinColumn(name="user_id", referencedColumnName="id")},
     *      inverseJoinColumns={@JoinColumn(name="address_id", referencedColumnName="id", unique=true)}
     * )
     */
    protected $addresses;
    // @todo: address owns user

    /**
     * @ManyToMany(targetEntity="Card")
     * @JoinTable(name="users_cards",
     *      joinColumns={@JoinColumn(name="user_id", referencedColumnName="id")},
     *      inverseJoinColumns={@JoinColumn(name="card_id", referencedColumnName="id", unique=true)}
     * )
     */
    protected $cards;
    // @todo: card owns user

    /**
    protected $cards;
     */

    /**
     * @Column(type="string")
     */
    protected $stripeToken;

    /**
     * @Column(type="string")
     */
    protected $facebookToken;

    /**
     * @Column(type="string")
     */
    protected $facebookId;

    public function __construct()
    {
        $this->addresses = new \Doctrine\Common\Collections\ArrayCollection();
        $this->cards     = new \Doctrine\Common\Collections\ArrayCollection();
    }

    public function getId()
    {
        return $this->id;
    }

    public function getFirstName()
    {
        return $this->firstName;
    }

    public function setFirstName( $firstName )
    {
        $this->firstName = $firstName;
    }

    public function getLastName()
    {
        return $this->lastName;
    }

    public function setLastName( $lastName )
    {
        $this->lastName = $lastName;
    }

    public function getEmail()
    {
        return $this->email;
    }

    public function setEmail( $email )
    {
        $this->email = $email;
    }

    public function getAddresses()
    {
        return $this->addresses;
    }

    public function addAddress( $address )
    {
        $this->addresses[] = $address;
    }

    public function getCards()
    {
        return $this->cards;
    }

    public function addCard( $card )
    {
        $this->cards[] = $card;
    }

    public function getStripeToken()
    {
        return $this->stripeToken;
    }

    public function setStripeToken( $stripeToken )
    {
        $this->stripeToken = $stripeToken;
    }

    public function getFacebookToken()
    {
        return $this->facebookToken;
    }

    public function setFacebookToken( $facebookToken )
    {
        $this->facebookToken = $facebookToken;
    }

    public function getFacebookId()
    {
        return $this->facebookId;
    }

    public function setFacebookId( $facebookId )
    {
        $this->facebookId = $facebookId;
    }

    public function jsonSerialize()
    {
        $info = array();

        $info['id']             = $this->getId();
        $info['firstName']      = $this->getFirstName();
        $info['lastName']       = $this->getLastName();
        $info['email']          = $this->getEmail();
        $info['addresses']      = array();
        $info['cards']          = array();
        $info['facebook_token'] = '';
        $info['facebook_id']    = '';

        $x = $this->getAddresses();
        /*
        if ( count( $x ) ) {
            foreach( $x as $y ) {
            }
        }
         */

        /*
        foreach( $this->getAddresses() as $address ) {
            //$info['addresses'][] = $address;
        }
         */

        foreach( $this->getCards() as $card ) {
            $info['cards'][] = $card;
        }

        return $info;
    }
}
