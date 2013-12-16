<?php
namespace DinDin\DinDin\Entities;
/**
 * @Entity @Table(name="cards")
 **/
class Card implements \JsonSerializable
{
    /** @Id @Column(type="integer") @GeneratedValue **/
    protected $id;

    /** @Column(type="string") **/
    protected $stripeId;

    /** @Column(type="integer") **/
    protected $last4;

    public function getId()
    {
        return $this->id;
    }

    public function setStripeId( $stripeId )
    {
        $this->stripeId = $stripeId;
    }

    public function getStripeId()
    {
        return $this->stripeId;
    }

    public function setLast4( $last4 )
    {
        return $this->last4 = $last4;
    }

    public function getLast4()
    {
        return $this->last4;
    }

    public function jsonSerialize()
    {
        $info = array();

        $info['id']    = $this->getId();
        $info['last4'] = $this->getLast4();

        return $info;
    }
}
