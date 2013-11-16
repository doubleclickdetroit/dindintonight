<?php
/**
 * @Entity @Table(name="users")
 */
class User
{
    /**
     * @Id @GeneratedValue @Column(type="integer")
     * @var int
     */
    protected $id;

    /**
     * @Column(type="integer")
     * @var int
     */
    protected $facebookId;

    /**
     * @Column(type="string")
     * @var string
     */
    protected $stripeToken;

    /**
     * @Column(type="string")
     * @var string
     */
    protected $name;

    /**
     * @OneToMany(targetEntity="Location", mappedBy="user")
     * @var Location[]
     **/
    protected $locations = null;

    public function getId()
    {
        return $this->id;
    }

    public function getFacebookId()
    {
        return $this->facebookId;
    }

    public function setFacebookId($facebookId)
    {
        $this->facebookId = $facebookId;
    }

    public function getStripToken()
    {
        return $this->stripeToken;
    }

    public function setStripeToken($stripeToken)
    {
        $this->stripeToken = $stripeToken;
    }

    public function getName()
    {
        return $this->name;
    }

    public function setName($name)
    {
        $this->name = $name;
    }
}
