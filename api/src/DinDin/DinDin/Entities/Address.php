<?php
namespace DinDin\DinDin\Entities;
/**
 * @Entity @Table(name="addresses")
 **/
class Address implements \JsonSerializable
{
    /** @Id @Column(type="integer") @GeneratedValue **/
    protected $id;

    /** @Column(type="text") **/
    protected $address;

    /**
     * @ManyToOne(targetEntity="Location")
     * @JoinColumn(name="location_id", referencedColumnName="id")
     */
    protected $location;

    public function getId()
    {
        return $this->id;
    }

    public function setAddress( $address )
    {
        $this->address = $address;
    }

    public function getAddress()
    {
        return $this->address;
    }

    public function setLocation( $location )
    {
        return $this->location = $location;
    }

    public function getLocation()
    {
        return $this->location;
    }

    public function jsonSerialize()
    {
        $info = array();

        $info['id']          = $this->getId();
        $info['address']     = $this->getAddress();
        $info['location_id'] = $this->getLocation()->getId();

        return $info;
    }
}
